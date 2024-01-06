function loadText(containerId, textFileURL) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", textFileURL, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var textContainer = document.getElementById(containerId);
            textContainer.innerHTML = "<p>" + xhr.responseText + "</p>";
        }
    };
    xhr.send();
}

document.addEventListener("DOMContentLoaded", function () {
    var textContainers = document.querySelectorAll('[data-textfile]');
    textContainers.forEach(function (container) {
        var containerId = container.id;
        var textFileURL = container.dataset.textfile;
        loadText(containerId, textFileURL);
    });
});