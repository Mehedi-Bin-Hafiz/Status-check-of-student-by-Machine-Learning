

      //alert("yoyo")
      var a=1

      function gogo(){
        var x=parseInt(document.getElementById('nono').value)
        // console.log(x);
        for(var i =0; i<10; i++)
        {
          for(var j=0; j<9; j++){
            x = x + Math.floor(Math.random()*4)+1
            console.log(a + ' - ' + x);
            a++
          }
          x = x + Math.floor(Math.random()*19) + 1
          console.log(a + ' - ' + x);
          a++
        }
        console.log("yohoho");
      }

