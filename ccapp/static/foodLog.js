var table  = document.getElementById('foodtable');
var calories = 0, fat = 0, carbs = 0, protein = 0;

for(var i = 1; i <table.rows.length - 1; i++) {
    calories += parseFloat(table.rows[i].cells[1].innerHTML);

    fat += parseFloat(table.rows[i].cells[2].innerHTML);
    fat = Math.round(fat);

    carbs += parseFloat(table.rows[i].cells[3].innerHTML);
    carbs = Math.round(carbs);

    protein += parseFloat(table.rows[i].cells[4].innerHTML);
    protein = Math.round(protein);    
}

document.getElementById('totalCalories').innerHTML = '<b>' + calories + '</b>';
document.getElementById('totalFat').innerHTML = '<b>' + fat + '</b>';
// document.getElementById('totalcarbs').innerHTML = '<b>' + carbs + '</b>';
document.getElementById('totalProtein').innerHTML = '<b>' + protein + '</b>';

var total = fat + carbs + protein;

var fatPercentage =  Math.round((fat / total) * 100);
var carbsPercentage =  Math.round((carbs / total) * 100);
var proteinPercentage =  Math.round((protein / total) * 100);

fatPercentage = fatPercentage ? fatPercentage : 0;
carbsPercentage = carbsPercentage ? carbsPercentage : 0;
proteinPercentage = proteinPercentage ? proteinPercentage : 0;
console.log(fatPercentage)

// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"';
Chart.defaults.global.defaultFontColor = 'white';

// Doughnut Chart - Macronutrients breakdown
var ctx = document.getElementById('myPieChart');
var myPieChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: [
            'Fat ' + fatPercentage + '%', 
            'Carbs ' +  carbsPercentage + '%', 
            'Protein ' + proteinPercentage + '%'
        ],
        datasets: 
        [
            {
                data: [fatPercentage, carbsPercentage, proteinPercentage],
                backgroundColor: ['pink', 'yellow', 'lightblue'],
            }
        ],
    },
    options: {
        responsive: true,
        maintainAspectRatio: true,
        animation: {
            animateScale: true,
        },
        plugins: {
            legend: {
                display: true,
                position: 'bottom',
            },
            title: {
                display: true,
                text: 'Macronutrients Breakdown',
                font: {
                    size: 20,
                },
            },
            datalabels: {
                display: true,
                color: '#fff',
                font: {
                    weight: 'bold',
                    size: 16,
                },
                textAlign: 'center',
            },
        },
    },
});



// Calorie Goal Progress Bar

var caloriePercentage = (calories / 2000) *  100;
//document.getElementById('progressBar').setAttribute('style', 'width:' + caloriePercentage + '%');

$('.progress-bar').animate({
    width: caloriePercentage + '%',

}, 500);
var interval = setInterval(function () {
$('.progress-bar').html(caloriePercentage + '%');

}, 500);