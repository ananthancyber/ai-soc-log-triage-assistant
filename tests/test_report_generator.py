import io

from app.report_generator import write_report


def test_write_report():

    report = io.StringIO()

    alert = {
        "rule": {
            "id": "5710",
            "description": "Multiple failed SSH login attempts"
        },
        "timestamp": "2026-08-04T18:00:00Z"
    }

    source_ip = "192.168.1.10"

    analysis = "This appears to be a brute-force login attempt."

    retrieved_documents = [
        {
            "document": "knowledge_base/ssh_authentication.md",
            "distance": 0.12
        }
    ]

    write_report(
        report,
        alert,
        source_ip,
        analysis,
        retrieved_documents
    )

    content = report.getvalue()

    assert "5710" in content
    assert "Multiple failed SSH login attempts" in content
    assert "192.168.1.10" in content
    assert "brute-force" in content