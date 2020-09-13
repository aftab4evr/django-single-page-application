$(document).ready(function () {
    var reverse = false;
    var index = 0;
    $('.sorting').on('click', function () {
        if (index == $(this).index() && reverse == false) {
            unSortTable($(this).index())
            reverse = true;
        } else {
            sortTable($(this).index())
            reverse = false;
            index = $(this).index();
        }
        addSerialNo();
    });
    
    function addSerialNo(){
        page=parseInt(getUrlParameter('page'))
        page=(page-1)*5
        table = document.getElementById("myTable");
        rows = table.rows;
        for(k=1;k<(rows.length);k++){
            rows[k].getElementsByTagName("td")[0].innerHTML=page+k
        }
    }
    function unSortTable(index) {
        var table, rows, unswitching, i, x, y, shouldSwitch;
        table = document.getElementById("myTable");
        unswitching = true;
        while (unswitching) {
            unswitching = false;
            rows = table.rows;
            for (i = 1; i < (rows.length - 1); i++) {
                shouldSwitch = false;
                x = rows[i].getElementsByTagName("td")[index];
                y = rows[i + 1].getElementsByTagName("td")[index];
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
            if (shouldSwitch) {
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                unswitching = true;
            }
        }
    }
    function sortTable(index) {
        var table, rows, switching, i, x, y, shouldSwitch;
        table = document.getElementById("myTable");
        switching = true;
        while (switching) {
            switching = false;
            rows = table.rows;
            for (i = 1; i < (rows.length - 1); i++) {
                shouldSwitch = false;
                x = rows[i].getElementsByTagName("td")[index];
                y = rows[i + 1].getElementsByTagName("td")[index];
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }

            if (shouldSwitch) {
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                switching = true;
            }
        }
    }
    function getUrlParameter(name) {
        name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
        var regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
        var results = regex.exec(location.search);
        return results === null ? 1 : decodeURIComponent(results[1].replace(/\+/g, ' '));
    };
});