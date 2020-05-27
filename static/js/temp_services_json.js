
fetch('services.json').then(function(response) {
  return response.json();
}).then(function(json) {
  let services = json;
  initialize(services);
}).catch(function(err) {
  console.log('Fetch problem: ' + err.message);
});


function initialize(services) {
  
  const category = document.querySelector('#category');
  const category = document.querySelector('#group');
  const searchTerm = document.querySelector('#searchTerm');
  const searchBtn = document.querySelector('button');
  const main = document.querySelector('main');

  let lastCategory = category.value;
  let lastSearch = '';

  
  let categoryGroup;
  let finalGroup;

  finalGroup = services;
  updateDisplay();

  categoryGroup = [];
  finalGroup = [];

  searchBtn.onclick = selectCategory;

  function selectCategory(e) {
    e.preventDefault();

    categoryGroup = [];
    finalGroup = [];
    if(category.value === lastCategory) {                                         
      return;
    } else {
      lastCategory = category.value;
      if(category.value === 'All') {
        finalGroup = services;
        updateDisplay();
      } else {
        let lowerCaseType = category.value.toLowerCase();
        for(let i = 0; i < services.length ; i++) {
          
          if(services[i].type === lowerCaseType) {
            finalGroup.push(services[i]);
          }
        }
        updateDisplay();
        //selectservices();
      }
    }
  }

function SearchService(){
  if(searchTerm.value.trim() === lastSearch)
    return;
  else{
    lastSearch = searchTerm.value.trim();
    selectservices();
  }
}


  function selectservices() {
    if(searchTerm.value.trim() === '') {
      finalGroup = categoryGroup;
      updateDisplay();
    } else {
     
      let lowerCaseSearchTerm = searchTerm.value.trim().toLowerCase();
      
      for(let i = 0; i < categoryGroup.length ; i++) {
        if(categoryGroup[i].name.indexOf(lowerCaseSearchTerm) !== -1) {
          finalGroup.push(categoryGroup[i]);
        }
      }
      updateDisplay();
    }

  }

  function updateDisplay() {
    while (main.firstChild) {
      main.removeChild(main.firstChild);
    }

    if(finalGroup.length === 0) {
      const para = document.createElement('p');
      para.textContent = 'No results to display!';
      main.appendChild(para);
    } else {
      for(let i = 0; i < finalGroup.length; i++) {
        showservice(finalGroup[i]);
      }
    }
  }


function showservice(service) {
    const section = document.createElement('section');
    const content = document.querySelector("#")
    
    

    main.appendChild(section);
    section.

















