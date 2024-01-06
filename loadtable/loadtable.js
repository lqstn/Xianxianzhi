function LoadCSV(containerId) {
    var tableContainer = document.getElementById(containerId);

    // 获取数据文件路径
    var csvFilePath = tableContainer.getAttribute('data-csvfile');

     // 使用fetch API读取CSV文件
     fetch(csvFilePath)
     .then(response => response.text())
     .then(csvContent => {
         // 解析 CSV 数据
         var data = parseCSV(csvContent);
         // 生成表格
         generateTable(tableContainer, data);
     })
     .catch(error => console.error('Error fetching CSV:', error));

}

// 解析 CSV 数据
function parseCSV(csvContent) {
    var rows = csvContent.split('\n');
    var data = [];

    for (var i = 0; i < rows.length; i++) {
        var cells = rows[i].split(',');
        data.push(cells);
    }

    return data;
}

// 生成表格
function generateTable(container, data) {
    var tableHTML = '<table border="1">';

    for (var i = 0; i < data.length; i++) {
        tableHTML += '<tr>';
        for (var j = 3; j < data[i].length; j++) {
            tableHTML += '<td>' + data[i][j] + '</td>';
        }
        tableHTML += '</tr>';
    }

    tableHTML += '</table>';
    container.innerHTML = tableHTML;
}


