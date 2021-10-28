'''
Copyright 2021 Flexera Software LLC
See LICENSE.TXT for full license text
SPDX-License-Identifier: MIT

Author : sgeary  
Created On : Wed Oct 27 2021
File : xlsx_formatting.py
'''

# Colors for report
reveneraGray = '#323E48'
white = '#FFFFFF'
black = '#000000'
p1LicenseColor = "#C00000"
p2LicenseColor = "#FFFF00"
p3LicenseColor= "#008000"
NALicenseColor = "#D3D3D3"
criticalVulnColor = "#400000"
highVulnColor = "#C00000"
mediumVulnColor = "#FFA500"
lowVulnColor = "#FFFF00"
noneVulnColor = "#D3D3D3"
approvedColor = "#008000"
rejectedColor = "#C00000"
draftColor = "#D3D3D3"

# The default cell formatting
standardCellFormatProperties = {}
standardCellFormatProperties["font_size"] = "10"
standardCellFormatProperties["bold"] = False
standardCellFormatProperties["font_color"] = black
standardCellFormatProperties["bg_color"] = white
standardCellFormatProperties["text_wrap"] = True
standardCellFormatProperties["valign"] = "vcenter"
standardCellFormatProperties["align"] = "center"
standardCellFormatProperties["border"] = True

# Cells that are bold text
boldCellFormatProperties = standardCellFormatProperties.copy()
boldCellFormatProperties["bold"] = True

# Cells that are hyperlinks
linkCellFormatProperties = standardCellFormatProperties.copy()
linkCellFormatProperties["font_color"] = "blue"
linkCellFormatProperties["underline"] = True

# Cells that are table headers
tableHeaderFormatProperties = standardCellFormatProperties.copy()
tableHeaderFormatProperties["font_size"] = "12"
tableHeaderFormatProperties["bold"] = True
tableHeaderFormatProperties["font_color"] = white
tableHeaderFormatProperties["bg_color"] = reveneraGray
tableHeaderFormatProperties["text_wrap"] = True

# Formatting for display project hierarchy
hierarchyCellFormatProperties = standardCellFormatProperties.copy()
hierarchyCellFormatProperties["font_size"] = "12"
hierarchyCellFormatProperties["bold"] = True
hierarchyCellFormatProperties["align"] = "left"
hierarchyCellFormatProperties["text_wrap"] = False
hierarchyCellFormatProperties["border"] = False
