/**
 * Created by LiYong on 2018/5/3.
 */
function changetext(id)
{
    id.innerHTML = "你点击了文本";
}
function checkCookies()
{
    if (navigator.cookieEnabled == true)
    {
        alert("Cookies 可用");
    }
    else
    {
        alert("Cookies 不可用");
    }
}
function myFounction()
{
    var x = document.getElementById("fname");
    x.value = x.value.toUpperCase();
}
