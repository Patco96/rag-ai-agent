from src.graph import graph

# Get the PNG data from the mermaid diagram
png_data = graph.get_graph(xray=True).draw_mermaid_png()

# Save the PNG data to a file
output_path = "graph_diagram.png"
with open(output_path, "wb") as f:
    f.write(png_data)
print(f"Diagram saved to {output_path}")
