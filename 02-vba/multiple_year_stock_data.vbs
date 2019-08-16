'Author - Tasneem

Sub multiple_year_stock_data()

'Variable declaration
'variable to hold the row for the Summary Details
Dim Summary_Table_Row As Integer
' Set an initial variable for holding the ticker name
Dim ticker_Name As String
' Set an initial variable for holding the total volume of stock
Dim volume_Total As Double
volume_Total = 0
Dim openingPrice As Double
openingPrice = 0
Dim closingPrice As Double
closingPrice = 0
Dim Percentage As Double

Percentage = 0
Dim Yearly_change As Double
Yearly_change = 0

'Variable Declaration to find the Max and Min Values
Dim MaxTotalVolum As Double
Dim MaxVolCell As Integer
Dim MaxPercent As Double
Dim MaxPercentCell As Integer
Dim MinPercent As Double
Dim MinPercentCell As Integer

Dim intRowVol As Integer


' --------------------------------------------
' LOOP THROUGH ALL SHEETS
' --------------------------------------------

For Each ws In Worksheets
    'Obtain the LastRow Count to initialize the loop to read the stock data
    LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    'Debug statement
    'MsgBox ("Last Row" & LastRow)
    ' Keep track of the location for each stock in the summary table

    'Header for the Summary Details
    ws.Range("J1").Value = "Ticker"
    ws.Range("K1").Value = "Yearly Change"
    ws.Range("L1").Value = "Percent Change"
    ws.Range("M1").Value = "Total Stock Volume"
    'Debug Purpose
    'ws.Range("N1").Value = "Opening Price"
    'ws.Range("O1").Value = "Closing Price"

    'Assigning value 2 so that it starts at row two after the header
    Summary_Table_Row = 2
    'Initializing all the values to 0 for each worksheet
    volume_Total = 0
    openingPrice = 0
    closingPrice = 0
    Percentage = 0
    Yearly_change = 0
   
   'Holding the opening price of first row and then start the loop
    openingPrice = ws.Cells(2, 3).Value

    For iRow = 2 To LastRow
        ' Add to the Volume Total
        volume_Total = volume_Total + ws.Cells(iRow, 7).Value
        
        ' Check if we are still within the same ticker, if it is not...
        If ws.Cells(iRow + 1, 1).Value <> ws.Cells(iRow, 1).Value Then
                
            ' Set the ticker name
                ticker_Name = ws.Cells(iRow, 1).Value
        
                closingPrice = ws.Cells(iRow, 6).Value
                'calculate the percentage
                
                Percentage = (closingPrice - openingPrice) / openingPrice
                
                'calculate the yearly change
                Yearly_change = closingPrice - openingPrice
                
                
            ' Print the Ticker Name, yearly change in the Summary Table
                ws.Range("J" & Summary_Table_Row).Value = ticker_Name
                'Debug Purpose
                'ws.Range("N" & Summary_Table_Row).Value = openingPrice
                'ws.Range("O" & Summary_Table_Row).Value = closingPrice
                ws.Range("K" & Summary_Table_Row).Value = Yearly_change
                ws.Range("K" & Summary_Table_Row).NumberFormat = "0.000000000"
                'Inorder to have green for positive and red for negative
                If Yearly_change > 0 Then
                    ws.Range("K" & Summary_Table_Row).Interior.ColorIndex = 4
                Else
                    ws.Range("K" & Summary_Table_Row).Interior.ColorIndex = 3
                End If
                
                'Print the Percentage and format it right
                ws.Range("L" & Summary_Table_Row).Value = Percentage
                ws.Range("L" & Summary_Table_Row).NumberFormat = "0.00%"
                
                ' Print the total volume of stock to the Summary Table
                ws.Range("M" & Summary_Table_Row).Value = volume_Total
            
                
            ' Add one to the summary table row
                Summary_Table_Row = Summary_Table_Row + 1
            ' Reset the Volume Total
                volume_Total = 0
            'Set the openingPrice of the next Ticker
                openingPrice = ws.Cells(iRow + 1, 3).Value
        End If
        
    Next iRow
    
    
    'Header for the Summary Details
    ws.Range("P2").Value = "Greatest % Increase"
    ws.Range("P3").Value = "Greatest % Decrease"
    ws.Range("P4").Value = "Greatest Total Volume"
    ws.Range("Q1").Value = "Ticker"
    ws.Range("R1").Value = "Value"

    'Obtaining the last row count of the new Summary Details
    inRowVol = ws.Cells(Rows.Count, "L").End(xlUp).Row
    'MsgBox ("Row count" & inRowVol)
    
    'Finding the Max Percentage
    MaxPercent = Application.WorksheetFunction.Max(ws.Range("L2:L" & inRowVol))
    ws.Range("R2").Value = MaxPercent
    ws.Range("R2").NumberFormat = "0.00%"
    MaxPercentCell = Application.WorksheetFunction.Match(MaxPercent, ws.Range("L2:L" & inRowVol), 0)
    'Adding one as we need to factor for the column header
    MaxPercentCell = MaxPercentCell + 1
    ws.Range("Q2").Value = ws.Range("J" & MaxPercentCell)
    
    'Obtaining the last row count of the new Summary Details.. doing again just incase
    inRowVol = ws.Cells(Rows.Count, "L").End(xlUp).Row
    'MsgBox ("Row count" & inRowVol)
    'Finding the Min Percentage
    MinPercent = Application.WorksheetFunction.Min(ws.Range("L2:L" & inRowVol))
    ws.Range("R3").Value = MinPercent
    ws.Range("R3").NumberFormat = "0.00%"
    MinPercentCell = Application.WorksheetFunction.Match(MinPercent, ws.Range("L2:L" & inRowVol), 0)
     'Adding one as we need to factor for the column header
    MinPercentCell = MinPercentCell + 1
    ws.Range("Q3").Value = ws.Range("J" & MinPercentCell)
               
    'Obtaining the last row count of the new Summary Details.. doing again just incase
    inRowVol = ws.Cells(Rows.Count, "M").End(xlUp).Row
    'MsgBox ("Row count" & inRowVol)
    
    'Find the Max Volume
    MaxTotalVolum = Application.WorksheetFunction.Max(ws.Range("M2:M" & inRowVol))
    
    ws.Range("R4").Value = MaxTotalVolum
    MaxVolCell = Application.WorksheetFunction.Match(MaxTotalVolum, ws.Range("M2:M" & inRowVol), 0)
    'Adding one as we need to factor for the column header
    MaxVolCell = MaxVolCell + 1
    ws.Range("Q4").Value = ws.Range("J" & MaxVolCell)


'Debug Purposes
'Exit For
Next ws
MsgBox ("All Done ..")
End Sub




