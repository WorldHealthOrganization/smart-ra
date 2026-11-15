| **Data element** | **Description** | **Requirement Status** |
| --- | --- | --- |
| **Generic product identifier** | The canonical, system-independent identifier for a product at generic level (e.g., amoxicillin 500mg capsule), independent of brand or manufacturer. | **Mandatory** |
| **Generic product description** | Human-readable description of the generic product, including key clinical attributes in standardised form. | **Mandatory** |
| **Item identifier (GTIN)** | Global Trade Item Number or equivalent standardised trade item identifier assigned at the specific product/brand/pack level. | **Mandatory** |
| **Brand name** | Proprietary or trade name of the product as registered by the manufacturer. | **Mandatory** |
| **Unit of measure** | The base unit in which the product is counted, dispensed, or issued (e.g., tablet, vial, sachet). | **Mandatory** |
| **Product classification** | Classification of the product under applicable schemes such as UNSPSC (pharmaceuticals), GPC (medical devices), or ATC (medicines). For medicinal products, alignment with the WHODrug data dictionary is recommended. Supports multi-classification. | **Mandatory** |
| **Dosage form** | Physical form of the product (e.g., tablet, capsule, oral solution, injection). | **Mandatory** |
| **Strength** | Quantity of active ingredient per unit of the product (e.g., 500mg, 10mg/mL). | **Mandatory** |
| **Manufacturer name** | Name of the legal manufacturer responsible for production of the item. | **Mandatory** |
| **Country of origin** | Country in which the product is manufactured. | **Mandatory** |
| **Route of administration** | How the product is intended to be administered (e.g., oral, intravenous, topical). | **Mandatory** |
| **Shelf life from production** | The maximum shelf life of the product from date of manufacture, expressed in months. | **Mandatory** |
| **Storage requirements** | Conditions under which the product must be stored, particularly temperature range (min/max) and humidity where applicable. | **Mandatory** |
| **Volumetrics** | Physical dimensions and weight of the product and its packaging levels, used for transport and storage capacity planning. | **Mandatory** |
| **Packaging hierarchy level** | Definition of the packaging levels (unit, inner pack, case, pallet) with the applicable GTIN and quantity conversion for each level. | **Mandatory** |
| **Generic product to item mapping** | The relationship between the generic product definition and the specific branded item(s) that fulfil it, supporting substitution and equivalence management. | **Mandatory** |
| **Brand mappings** | Cross-references between a generic product identifier and all known brand/trade names under which it is marketed. | **Recommended** |
| **Item registration details** | Regulatory registration or marketing authorisation details for the product, including registration number, registering authority, and expiry date. | **Recommended** |
