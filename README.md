# FastBox Delivery System

This is my Python solution for the FastBox Mystery Delivery System assignment.

## How it works

The program reads the delivery details from a JSON file and processes the packages one by one.

For every package:

1. It finds the package warehouse.
2. It checks the distance from each agent's current position to that warehouse.
3. The nearest agent gets the package.
4. The agent travels to the warehouse and then to the destination.
5. After delivery, the destination becomes the agent's new position.

The program then calculates the total distance and the average distance per package for each agent.

## Distance formula

Euclidean distance is used:

`distance = sqrt((x2-x1)^2 + (y2-y1)^2)`

## Run the program

You need Python 3 installed.

```bash
python main.py test_cases/test_case_1.json
```

A `report.json` file will be created in the same folder as the input file.

## Project files

```text
FastBox-Delivery-System/
|
|-- main.py
|-- README.md
|-- .gitignore
|-- test_cases/
|   |-- test_case_1.json
|   |-- test_case_2.json
|   |-- ...
|   `-- test_case_10.json
|
`-- reports/
    |-- test_case_1_report.json
    |-- ...
    `-- test_case_10_report.json
```

## Complexity

If there are `P` packages and `A` agents, the program checks every agent for every package.

Time complexity: `O(P * A)`

Space complexity: `O(P + A)`

## GitHub upload

After creating a new repository on GitHub, run:

```bash
git init
git add .
git commit -m "Add FastBox delivery system"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

Replace `YOUR_REPOSITORY_URL` with your own GitHub repository URL.
