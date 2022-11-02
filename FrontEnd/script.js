var array=["News","News","News","News","News","News","News","News","News"];
var descarr=["Trump urged armed supporters to storm Capitol - aide",
                "Migrants die daily in lorries hot as 'gates of hell'",
            "Kremenchuk.: Strike on shopping centre was act of terror - Zelensky",
            "Ghislaine Maxwell awaits sentencing over sex trafficking charge",
            "'We still want answers from Maxwell'",
            "Ghislaine Maxwell: What sentencing means to women she preyed on",
            "Scottish independence: 19 October 2023 proposed as date for referendum",
            "Texas migrant deaths: At least 50 found dead in abandoned truck",
            "F1 condemns Piquet's racist language about Hamilton",
           
        ];

var dynamic=document.querySelector('.row');
for(var i=0;i<array.length;i++)
{   var fetch=document.querySelector('.row').innerHTML;
    dynamic.innerHTML=` <div class="column">
    
    <div class="card">
      <br>
   
      <h2 >${array[i]}</h2>
      <p >${descarr[i]}</p>
    
    
    </div>
  </div>`+fetch;
}