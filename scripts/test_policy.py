"""Exercise the trusted workflow's actual shell policy with a local API double."""

import json
import os
import shutil
import subprocess  # nosec B404
import tempfile
import unittest
from pathlib import Path

import yaml
from validate import ROOT


@unittest.skipUnless(os.name == "posix" and shutil.which("bash") and shutil.which("jq"),
                     "Workflow shell test requires Linux bash/jq; exercised in GitHub CI")
class PromotionPolicyTests(unittest.TestCase):
    def test_trusted_policy_does_not_checkout_or_run_pr_files(self):
        workflow = yaml.safe_load((ROOT / ".github/workflows/main-source.yml").read_text())
        steps = workflow["jobs"]["promotion"]["steps"]
        self.assertEqual(workflow["permissions"], {"contents": "read", "statuses": "write"})
        self.assertEqual(len(steps), 1)
        self.assertNotIn("uses", steps[0])
        self.assertNotIn("checkout", steps[0]["run"])
        self.assertNotIn("GITHUB_WORKSPACE", steps[0]["run"])

    def test_only_same_repository_dev_passes_and_publishes_status(self):
        workflow = yaml.safe_load((ROOT / ".github/workflows/main-source.yml").read_text())
        script = workflow["jobs"]["promotion"]["steps"][0]["run"]
        with tempfile.TemporaryDirectory() as directory:
            temp = Path(directory)
            api = temp / "gh"
            api.write_text('#!/bin/bash\nfor arg in "$@"; do last="$arg"; done\n'
                           'cp "$last" "$CAPTURE_STATUS"\n', encoding="utf-8")
            api.chmod(0o700)
            for branch, repository, allowed in (
                ("dev", "owner/skill", True),
                ("feature/change", "owner/skill", False),
                ("dev", "fork/skill", False),
                ("main", "owner/skill", False),
            ):
                with self.subTest(branch=branch, repository=repository):
                    env = {**os.environ, "PATH": str(temp) + os.pathsep + os.environ["PATH"],
                           "RUNNER_TEMP": str(temp), "CAPTURE_STATUS": str(temp / "status.json"),
                           "TARGET_REPO": "owner/skill", "HEAD_REPO": repository,
                           "HEAD_BRANCH": branch, "HEAD_SHA": "a" * 40}
                    # Execute trusted repository policy with a local API double.
                    result = subprocess.run([shutil.which("bash"), "-c", script], env=env,  # nosec B603
                                            capture_output=True, text=True, timeout=10, check=False)
                    self.assertEqual(result.returncode == 0, allowed, result.stderr)
                    status = json.loads((temp / "status.json").read_text())
                    self.assertEqual(status["state"], "success" if allowed else "failure")
                    self.assertEqual(status["context"], "main-source-policy")


if __name__ == "__main__":
    unittest.main()
