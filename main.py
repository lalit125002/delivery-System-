import json
import math
import sys
from pathlib import Path


def distance(p1, p2):
    """Find the distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def solve(data):
    agents = data["agents"]
    warehouses = data["warehouses"]
    packages = data["packages"]

    # Keep track of where every agent is currently located.
    current = {name: list(pos) for name, pos in agents.items()}
    delivered = {name: 0 for name in agents}
    total = {name: 0.0 for name in agents}

    for package in packages:
        warehouse = warehouses[package["warehouse"]]

        # Choose the closest agent to the warehouse.
        chosen = None
        shortest = None
        for name in agents:
            d = distance(current[name], warehouse)
            if shortest is None or d < shortest:
                shortest = d
                chosen = name

        destination = package["destination"]

        # Agent goes to the warehouse and then to the destination.
        total[chosen] += distance(current[chosen], warehouse)
        total[chosen] += distance(warehouse, destination)
        current[chosen] = list(destination)
        delivered[chosen] += 1

    result = {}
    for name in agents:
        count = delivered[name]
        result[name] = {
            "packages_delivered": count,
            "total_distance": round(total[name], 2),
            "efficiency": round(total[name] / count, 2) if count else None
        }

    active_agents = [name for name in agents if delivered[name] > 0]
    if active_agents:
        best = min(active_agents, key=lambda name: (result[name]["efficiency"], name))
        result["best_agent"] = best
    else:
        result["best_agent"] = None

    return result


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input.json>")
        return

    file_name = Path(sys.argv[1])

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)

        result = solve(data)

        output_file = file_name.with_name("report.json")
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4)

        print(json.dumps(result, indent=4))
        print("\nReport saved in:", output_file)

    except FileNotFoundError:
        print("Input file not found:", file_name)
    except json.JSONDecodeError:
        print("The input file is not valid JSON.")
    except KeyError as error:
        print("Missing key in input:", error)


if __name__ == "__main__":
    main()
