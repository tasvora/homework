// @TODO: YOUR CODE HERE!
// Step 1: Set up our chart
//= ================================
var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 50
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Step 2: Create an SVG wrapper,
// append an SVG group that will hold our chart,
// and shift the latter by left and top margins.
// =================================
var svg = d3.select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Initial Choosen XAxis Params
var chosenXAxis = "poverty";
var chosenYAxis = "healthcare";



// function used for updating x-scale var upon click on axis label
// Step 5: Create the scales for the chart
// =================================
function xScale(stateData, chosenXAxis) {

  var xLinearScale = d3.scaleLinear()
    .domain([8.5, d3.max(stateData, d => d[chosenXAxis])])
    .range([0, width]);

  return xLinearScale;

}

function yScale(stateData, chosenYAxis) {

  var yLinearScale = d3.scaleLinear()
    .domain([3, d3.max(stateData, d => d[chosenYAxis])])
    .range([height, 0]);

  return yLinearScale;

}

// function used for updating xAxis var upon click on axis label
function renderAxes(newXScale, xAxis) {
  var bottomAxis = d3.axisBottom(newXScale);

  xAxis.transition()
    .duration(1000)
    .call(bottomAxis);

  return xAxis;


  // var xAxis = chartGroup.append("g")
  //   .attr("transform", `translate(0, ${height})`)
  //   .call(bottomAxis);
}

// function used for updating circles group with a transition to
// new circles
function renderCircles(circlesGroup, newXScale, newYScale, chosenXaxis) {

  circlesGroup.transition()
    .duration(1000)
    .attr("cx", d => newXScale(d[chosenXAxis]))
    .attr("cy", d => newYScale(d[chosenYAxis]));

  return circlesGroup;
}

function renderCircleText(circleText, newXScale, newYScale, chosenXaxis) {

  circleText.transition()
    .duration(1000)
    .attr("x", d => newXScale(d[chosenXAxis]))
    .attr("y", d => newYScale(d[chosenYAxis]))
    .text(function (d) { return d.abbr; });

  return circleText;
}

// Step 3:
// Import data from the donuts.csv file
// =================================
d3.csv("assets/data/data.csv").then(function (stateData) {
  // Step 4: Parse the data
  // Format the data and convert to numerical and date values
  // =================================
  // Format the data
  stateData.forEach(function (data) {

    data.poverty = +data.poverty;
    data.healthcare = +data.healthcare;
    data.obesity = +data.obesity;
    data.smokes = +data.smokes;
    data.age = +data.age;
    data.income = +data.income;
  });

  // xLinearScale function above csv import
  var xLinearScale = xScale(stateData, chosenXAxis);

  var yLinearScale = yScale(stateData, chosenYAxis);


  // Step 7: Create the axes
  // =================================
  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);

  // Step 4: Append Axes to the chart
  // ==============================
  var xAxis = chartGroup.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);

  chartGroup.append("g")
    .call(leftAxis);

  // Step 5: Create Circles
  // ==============================
  var circlesGroup = chartGroup.selectAll("blah")
    .data(stateData)
    .enter()


  circlesGroup
    .append("circle")
    .attr("cx", d => xLinearScale(d[chosenXAxis]))
    .attr("cy", d => yLinearScale(d[chosenYAxis]))
    .attr("r", "15")
    .attr("fill", "blue")
    .attr("opacity", ".5")


  //  circlesGroup.append("text").text(function (d) { return d.abbr; });

  //Resources -- https://stackoverflow.com/questions/26955267/adding-text-to-a-circle-in-d3
  var circleText = chartGroup.selectAll()
    .data(stateData)
    .enter()
    .append("text")
    .attr("x", d => xLinearScale(d[chosenXAxis]))
    .attr("y", d => yLinearScale(d[chosenYAxis]))
    .text(function (d) { return d.abbr; })
    .attr("font-family", "Courier")
    .attr("fill", "white")
    .attr("font-size", "10px")
    .attr("text-anchor", "middle");


  // Create group for  2 x- axis labels
  var xlabelsGroup = chartGroup.append("g")
    .attr("transform", `translate(${width / 2}, ${height + 20})`);

  var PovertydataLabel = xlabelsGroup.append("text")
    .attr("x", 0)
    .attr("y", 20)
    .attr("value", "poverty") // value to grab for event listener
    .classed("active", true)
    .text("Poverty %");

  var agedataLabel = xlabelsGroup.append("text")
    .attr("x", 0)
    .attr("y", 40)
    .attr("value", "age") // value to grab for event listener
    .classed("inactive", true)
    .text("Age Median");


  // append y axis.
  chartGroup.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .classed("axis-text", true)
    .text("Health Care");

  // x axis labels event listener
  xlabelsGroup.selectAll("text")
    .on("click", function () {
      // get value of selection
      var value = d3.select(this).attr("value");
      if (value !== chosenXAxis) {

        // replaces chosenXAxis with value
        chosenXAxis = value;

        // console.log(chosenXAxis)

        // functions here found above csv import
        // updates x scale for new data
        xLinearScale = xScale(stateData, chosenXAxis);

        // updates x axis with transition
        xAxis = renderAxes(xLinearScale, xAxis);

        // updates circles with new x values
        circlesGroup = renderCircles(circlesGroup, xLinearScale, yLinearScale, chosenXAxis);
        circleText = renderCircleText(circleText,xLinearScale,yLinearScale, chosenXAxis);
        
        // changes classes to change bold text
        if (chosenXAxis === "poverty") {
          PovertydataLabel
            .classed("active", true)
            .classed("inactive", false);
          agedataLabel
            .classed("active", false)
            .classed("inactive", true);
        }
        else {
          agedataLabel
            .classed("active", true)
            .classed("inactive", false);
          PovertydataLabel
            .classed("active", false)
            .classed("inactive", true);
        }
      }
    });

}).catch(function (error) {
  console.log(error);
});
