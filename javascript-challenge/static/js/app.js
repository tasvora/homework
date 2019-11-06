// from data.js
var tableData = data;


// YOUR CODE HERE!
var filter_button = d3.select("#filter-btn");
var reset_button = d3.select("#reset1-btn");
var ufoData_table = d3.select("#ufo-table");
var tbody = d3.select("tbody");
var countryList = d3.select("countrySelect");


var countryName = tableData.map(row => row.country);
countryList.append('option').text("").attr('value', "");
for(i=0;i<countryName.length;i++)
{
    countryList.append('option').text(countryName[i].toUpperCase()).attr('value', countryName[i]);
}


function build_ufo_table(initData)
{
    // tbody.html(" ");   
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

reset_button.on("click", function() {
    d3.event.preventDefault();
      console.log("Reset Clicked");
    d3.select("#datetime").node().value="";
  });

build_ufo_table(tableData);

filter_button.on("click", function() {

    d3.event.preventDefault();
    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");
    var inputValue = inputElement.property("value").trim();

    var inputCity = d3.select("#city").property("value").trim();
  
    console.log(inputValue);
    console.log(inputCity);
    
       tbody.html(" ");
    // Get the value property of the input element
  
    // Use the form input to filter the data by blood type
  //  var  filterUFO_Date = tableData;
    
    if(inputValue != "" && inputCity != "")
    {
        var  filterUFO_Date = tableData.filter(ufoRow => ufoRow.datetime == inputValue);
        var  filterUFO_City = filterUFO_Date.filter(ufoRow => ufoRow.city == inputCity);
//    console.log(filterUFO);
        build_ufo_table(filterUFO_City);
    }
    if(inputValue != "" || inputCity != "")
    {   
        var filterUFO_Date;
        if(inputValue != "")
        {
            filterUFO_Date = tableData.filter(ufoRow => ufoRow.datetime == inputValue);
            //build_ufo_table(filterUFO_Date);
        }else { filterUFO_Date = tableData; }
        if( inputCity != "")
        {
            var  filterUFO_City = filterUFO_Date.filter(ufoRow => ufoRow.city == inputCity);
            //build_ufo_table(filterUFO_City)
        }else { filterUFO_City = filterUFO_Date; }
        build_ufo_table(filterUFO_City);
    }
    else {
        var row = tbody.append("tr");
        row.append("td").text("No Search Results Found");
    }
        // filterUFO.forEach((filterData) => {
        //     var row1 = tbody.append("tr");
            
        //     console.log(`the datetime is ${filterData.datetime}`);
        //     console.log(`the city is ${filterData.city}`);
        //     console.log(`the state is ${filterData.state}`);
        //     console.log(`the country is ${filterData.country}`);
        //     console.log(`the shape is ${filterData.shape}`);
        //     row1.append("td").text(filterData.datetime);
        //     row1.append("td").text(filterData.city);
        //     row1.append("td").text(filterData.state);
        //     row1.append("td").text(filterData.country);
        //     row1.append("td").text(filterData.shape);
        //     row1.append("td").text(filterData.durationMinutes);
        //     row1.append("td").text(filterData.comments);
        // });
  });

  


