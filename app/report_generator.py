def write_report(report, alert, source_ip, analysis):
    """
    Write one alert analysis to the Markdown report.
    """

    report.write(f"## Rule ID: {alert['rule']['id']}\n")
    report.write(f"**Description:** {alert['rule']['description']}\n\n")
    report.write(f"**Source IP:** {source_ip}\n\n")
    report.write(f"**Timestamp:** {alert['timestamp']}\n\n")

    report.write("## AI Analysis\n\n")
    report.write(analysis)
    report.write("\n\n---\n\n")