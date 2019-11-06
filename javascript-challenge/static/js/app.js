//Javascript file to display UFO Sighting data.
// data objtained from data.js
var tableData = data;


// Variable values obtained from the index.html
var filter_button = d3.select("#filter-btn");
var reset_button = d3.select("#reset-btn");
var ufoData_table = d3.select("#ufo-table");
var tbody = d3.select("tbody");

//Function to create the table filled with data for the first load, or at every refresh.
function build_ufo_table(initData)
{
    tbody.html(" ");
    console.log(initData);
    var row = tbody.append("tr");
    initData.forEach((rowData) => {
        var row = tbody.append("tr");
        row.append("td").text(rowData.datetime);
        row.append("td").text(rowData.city);
        row.append("td").text(rowData.state);
        row.append("td").text(rowData.country);
        row.append("td").text(rowData.shape);
        row.append("td").text(rowData.durationMinutes);
        row.append("td").text(rowData.comments);     
    });
}

//Calling the build table function.
build_ufo_table(tableData);


//Function to be called on CLick of the filter table button.
//This function filters default ufo data based on datetime and then on city.
//In event that datatime is not entered the data will be filtered on city.

filter_button.on("click", function() {

    d3.event.preventDefault();
    // Select the input element and get the raw HTML node
    //obtain the date from input
    var inputDate = d3.select("#datetime").property("value").trim();
    // obtain the city from input
    var inputCity = d3.select("#city").property("value").trim();
  
    console.log(inputDate);
    console.log(inputCity);
    
    //    tbody.html(" ");
    //If date and city both are not empty then do the below 
    if(inputDate != "" && inputCity != "")
    {  
        //filter data based on date entered
        var  filterUFO_Date = tableData.filter(ufoRow => ufoRow.datetime == inputDate);
        //and then filter data based on city entered.
        var  filterUFO_City = filterUFO_Date.filter(ufoRow => ufoRow.city == inputCity);
        //build the table
        build_ufo_table(filterUFO_City);
    }
    //if either date or city have been entered and not both then do the below
    if(inputDate != "" || inputCity != "")
    {   
        //declare a object to hold filtered data based on date
        var filterUFO_Date;
        //if date has been entered filter the data else set the 
        //filtered date data as default data.
        if(inputDate != "")
        {
            filterUFO_Date = tableData.filter(ufoRow => ufoRow.datetime == inputDate);
            //build_ufo_table(filterUFO_Date);
        }else { filterUFO_Date = tableData; }
        //if city has been entered filter the previously filtered date dataset further
        if( inputCity != "")
        {
            var  filterUFO_City = filterUFO_Date.filter(ufoRow => ufoRow.city == inputCity);
            //build_ufo_table(filterUFO_City)
        }else { filterUFO_City = filterUFO_Date; }
        //Now build the table.
        build_ufo_table(filterUFO_City);
    }
    else {
        var row = tbody.append("tr");
        row.append("td").text("No Search Results Found");
    }
  });


//Function to be called on CLick of the Reset table button.
//This function cleans the data in the date and city feild.
//And resets the table to default.

  reset_button.on("click", function() {
    d3.event.preventDefault();
    console.log("Reset Clicked");
    d3.select("#datetime").node().value="";
    d3.select("#city").node().value="";
    build_ufo_table(tableData);
  });



