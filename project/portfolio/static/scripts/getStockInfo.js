const ALPHAVANTAGE_API_KEY = <your api key goes here>;

async function getStockData(symbol) {
    const response = await fetch(`https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=${symbol}&apikey=${ALPHAVANTAGE_API_KEY}`);

    if (response.status === 200) {
        const data = await response.json();
        return data;
    }
}

async function createChart(symbol) {
    const data = await getStockData(symbol);

    const stockHistory = data['Time Series (Daily)'];

    // create chart from data
    if (stockHistory) {

        const stockData = [...Object.values(stockHistory)].slice(0, 7).reverse();

        const parsedData = stockData.map((day, i) => {
            const open = Number(day['1. open']);
            const high = Number(day['2. high']);
            const low = Number(day['3. low']);
            const close = Number(day['4. close']);

            return [i, high, open, close, low];
        });

        const chartData = google.visualization.arrayToDataTable(parsedData, true);

        const options = {
            legend: 'none',
            bar: { groupWidth: '100%' },
            candlestick: {
                fallingColor: { strokeWidth: 0, fill: '#a52714' }, // red
                risingColor: { strokeWidth: 0, fill: '#0f9d58' }   // green
            }
        };

        const chartDiv = document.createElement('div');

        const chart = new google.visualization.CandlestickChart(chartDiv);
        chart.draw(chartData, options);

        return chartDiv;
    }
}

async function addChartToDocument(symbol) {
    const chartDiv = await createChart(symbol);

    const dest = document.getElementById('featured');

    if (chartDiv) {
        dest.appendChild(chartDiv);
    } else {
        const emptyDiv = document.createElement('div');
        const textNode = document.createTextNode('Cannot display chart');
        emptyDiv.appendChild(textNode);

        dest.appendChild(emptyDiv);
    }
}

google.charts.load('current', {'packages':['corechart']});

const featured = ['MSFT', 'AAPL'];
google.charts.setOnLoadCallback(() => {
    featured.forEach(addChartToDocument);
});