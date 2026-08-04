from app.prompt_builder import build_prompt


def test_build_prompt_contains_alert_description():

   alert = {
    "rule": {
        "id": "5710",
        "description": "Multiple failed SSH login attempts"
    },
    "timestamp": "2026-08-04T18:00:00Z"
    }

   source_ip = "192.168.1.10"

   knowledge = "SSH brute force attacks are common."

   prompt = build_prompt(
        alert,
        source_ip,
        knowledge
    )

   assert "Multiple failed SSH login attempts" in prompt
   assert "192.168.1.10" in prompt
   assert "SSH brute force attacks are common." in prompt