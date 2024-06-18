import netmonitor.data_collection as dc
import netmonitor.data_analysis as da
import netmonitor.visualization as vis

# Example usage
data = dc.collect_data('eth0', 100)
summary = da.analyze_traffic(data)
vis.plot_traffic_summary(summary)
anomalies = da.detect_anomalies(data)
vis.plot_anomalies(anomalies)
