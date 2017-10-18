var resultado;


$.ajax({
  url:'http://localhost:8000/api/',
  success: function(result){
    if(result){
      console.log(result);
    }
  resultado = result;

  }
});
