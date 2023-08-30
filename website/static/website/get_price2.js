(function(){   
    
    document.querySelector('#addtest').addEventListener("click", function(event){
        event.preventDefault();
        //console.log(event.target);
        let element = document.querySelector('#test_select')
        let price = element.options[element.selectedIndex].getAttribute("data-price");
        let test = element.options[element.selectedIndex].value
        console.log(test, price);
        element = document.querySelector("#pricetablebody");
        let tr = document.createElement("tr");
        tr.innerHTML = `<td>${test}</td>
                        <td>${price}</td>`;
        element.append(tr);
        total = document.querySelector("#total").innerHTML;
        total = parseInt(total) + parseInt(price);
        document.querySelector("#total").innerHTML = total;
    });

    
})()



/*



el = document.getElementById('test_select');
    dl = document.getElementById('testlist');
    function AddValue(el, dl){
        if(el.value.trim() != ''){
          var opSelected = dl.querySelector(`[value="${el.value}"]`);
          var option = document.createElement("option");
          option.value = opSelected.value;
          option.text = opSelected.getAttribute('label');
          document.getElementById('Colors').appendChild(option);
        }
      }
    

*/