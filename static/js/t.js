function total()
{
  var sum = document.getElementById("sum");
  var table = document.getElementById("table");
  var sum1 = 0;
  var sum2=0;
  for(var i=1; i<table.rows.length; ++i) {
    sum1 += parseInt(table.rows[i].cells[2].innerHTML);
    sum2 += parseInt(table.rows[i].cells[3].innerHTML);
  }
  var sum3=(sum1-sum2);
  if(sum3>=0)
  {
    sum.innerText="There is a projected budget surplus of $"+sum3;
  }
  else {
    sum.innerText="There is a projected budget deficit of $"+sum3;
  }

}
