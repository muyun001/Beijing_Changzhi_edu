// 选择班级的复选框的点击事件
function checkboxOnclick(checkbox) {
    "use strict";
    if (checkbox.checked === true) {
        document.getElementById("table").style.display = "block";
    } else {
        document.getElementById("table").style.display = "none";
    }
}

