# Data Description

## Overview

The dataset used in this project contains information about greenhouse gas emissions across various countries and years. 
It provides insights into the amount of greenhouse gases emitted, measured in kilotonnes of CO2 equivalent.

## Dataset Details

- **File**: `data.csv`
- **Source**: [UN Climate Change](https://di.unfccc.int/time_series)

The Greenhouse Gas (GHG) Inventory Data contains the most recently submitted information, covering the period from 1990 
to the latest available year, to the extent the data have been provided. The GHG data contain information on 
anthropogenic emissions by sources and removals by sinks of the following GHGs (carbon dioxide (CO2), methane (CH4), 
nitrous oxide (N2O), hydrofluorocarbons (HFCs), perfluorocarbons (PFCs), unspecified mix of HFCs and PFCs, sulphur 
hexafluoride (SF6) and nitrogen triflouride (NF3)) that are not controlled by the Montreal Protocol.

GHG emission inventories are developed by Parties to the Convention using scientific and methodological guidance from 
the Intergovernmental Panel on Climate Change (IPCC), such as 2006 IPCC Guidelines for National Greenhouse Gas 
Inventories, Revised Guidelines for National Greenhouse Gas Inventories (1996), IPCC Good Practice Guidance and 
Uncertainty Management in National Greenhouse Gas Inventories (2000), IPCC Good Practice Guidance on Land Use, Land-use 
Change and Forestry (2003) and 2013 Supplement to the 2006 IPCC Guidelines for National Greenhouse Gas Inventories: 
Wetlands.

Last update in UNdata: 2023/11/22
Next update in UNdata: 2024/12/01

### Columns

1. **Country or Area**: The name of the country or region reporting the emissions.
2. **Year**: The year for which the emissions data is reported.
3. **Value**: The amount of greenhouse gas emissions, originally in tonnes. This value is converted to kilotonnes for 
     analysis.

### Data Example

| Country or Area | Year | Value   |
|-----------------|------|---------|
| USA             | 2019 | 500000  |
| China           | 2019 | 1000000 |
| India           | 2020 | 600000  |

### Data Cleaning

- **Renamed Columns**: 'Value' to 'Amount', 'Country or Area' to 'Country'.
- **Unit Conversion**: The 'Amount' column is converted from tonnes to kilotonnes.
- **Year Format**: The 'Year' column is converted to a period index with annual frequency.

### Notes

Ensure the dataset is placed in the `data` folder and named `data.csv` before running the analysis script.
