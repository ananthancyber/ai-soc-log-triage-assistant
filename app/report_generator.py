def write_report(
    report,
    alert,
    source_ip,
    analysis,
    retrieved_documents
):
    """
    Write one alert analysis to the Markdown report.
    """
    report.write("---" * 80 + "\n\n")
    report.write(f"# Alert {alert['rule']['id']}\n\n")
    report.write(f"**Description:** {alert['rule']['description']}\n\n")
    report.write(f"**Source IP:** {source_ip}\n\n")
    report.write(f"**Timestamp:** {alert['timestamp']}\n\n")
    report.write("---\n\n")
    report.write("## Retrieved Knowledge Sources\n\n")

    for item in retrieved_documents:
      report.write(
        f"- {item['document']} "
        f"(Distance: {item['distance']:.4f})\n"
    )

    report.write("\n")
    report.write("## AI Analysis\n\n")
    report.write(analysis)
    report.write("\n\n---\n\n")