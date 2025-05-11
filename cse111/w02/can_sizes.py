import math

def main():
    can_names = [
        "#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5",
        "#6Z", "#8Z short", "#10", "#211", "#300", "#303"
    ]
    can_radiuses = [
        6.83, 7.78, 8.73, 10.32, 10.79, 13.02,
        5.4, 6.83, 15.72, 6.83, 7.62, 8.1
    ]
    can_heights = [
        10.16, 11.91, 11.59, 11.91, 17.78, 14.29,
        8.89, 7.62, 17.78, 12.38, 11.27, 11.11
    ]
    can_costs = [
        0.28, 0.43, 0.45, 0.61, 0.86, 0.83,
        0.22, 0.26, 1.53, 0.34, 0.38, 0.42
    ]

    best_store_name = ""
    best_cost_name = ""
    max_store_eff = -1
    max_cost_eff = -1

    print(f"{'Can Name':<15}{'Storage Efficiency':<15}{'Cost Efficiency':<15}")
    print("-" * 60)

    for i in range(len(can_names)):
        name = can_names[i]
        radius = can_radiuses[i]
        height = can_heights[i]
        cost = can_costs[i]

        store_eff = compute_storage_efficiency(radius, height)
        cost_eff = compute_cost_efficiency(radius, height, cost)

        print(f"{name:<15}{store_eff:.4f}{cost_eff:.2f}")

        if store_eff > max_store_eff:
            best_store_name = name
            max_store_eff = store_eff

        if cost_eff > max_cost_eff:
            best_cost_name = name
            max_cost_eff = cost_eff

    print("\nBest can size in storage efficiency:", best_store_name)
    print("Best can size in cost efficiency:", best_cost_name)

def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    return volume / surface_area

def compute_cost_efficiency(radius, height, cost):
    volume = compute_volume(radius, height)
    return volume / cost

def compute_volume(radius, height):
    return math.pi * radius**2 * height

def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

main()
