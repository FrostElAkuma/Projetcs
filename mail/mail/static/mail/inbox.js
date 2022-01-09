document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  //When you submit the composed email
  //Spent 1 hour on this as well. It is form on submit and not button on click like i had :D
  document.querySelector('form').onsubmit = send_email;

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#inside-mail-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}



function load_mailbox(mailbox) {
  let counter = 0;
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#inside-mail-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
   
   //if yu want to use a var inside you need to use `` instead of ''
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(email => {
      // Print email
      console.log(email);
      //Creating a div for each email
      email.forEach(element => {
        counter ++;

        const id = element.id
        const sender = element.sender;
        const subject = element.subject;
        const time = element.timestamp;
        const  recipients = element.recipients;
        const body = element.body;
        const div = document.createElement('div');
        const divOG = document.createElement('div');
        const btn = document.createElement('button');
        const hr = document.createElement('hr');
        const archived = element.archived;
        const read = element.read;
        
        //for styling later
        div.className = "emailDiv"
        divOG.className = `OG${counter}`
        btn.className = "archBtn btn btn-secondary"

        //I am doing this so each button and email can be in 1 div
        if (mailbox === 'inbox' || mailbox === 'archive' || mailbox === 'sent'){
          document.querySelector('#emails-view').append(divOG, hr);
        }
        //Deciding what div template to load based on the mailbox view
        if (mailbox === 'sent'){
          div.innerHTML = `<div>${recipients} &emsp;&emsp;${subject} &emsp;&emsp;${time}</div>`;
        } else if (mailbox === 'inbox') {
          div.innerHTML = `<div>${sender} &emsp;&emsp;${subject} &emsp;&emsp;${time}</div>`;
          btn.innerHTML = `Archive Email`
        } else {
          div.innerHTML = `<div>${sender} &emsp;&emsp;${subject} &emsp;&emsp;${time}</div>`;
          btn.innerHTML = `Unarchive Email`
        }

        //Archiving mail from inbox
        btn.addEventListener('click', () => archive(id, archived));
        //Making the email read if clicked on and opening the email to show its contents
        div.addEventListener('click', function() {
          //Making it read once clicked on
          fetch(`/emails/${id}`, {
            method: 'PUT',
            body: JSON.stringify({
                read: true
            })
          })
          
          
          //Getting the inside mail view
          console.log('This element has been clicked!')

          document.querySelector('#emails-view').style.display = 'none';
          document.querySelector('#compose-view').style.display = 'none';
          document.querySelector('#inside-mail-view').style.display = 'block';
          //Determining weather to show archive or unarchive inside the button
          let arch = "Archive"
          if (archived === true) {
            arch = "Unarchive"
          }
          //Filling the inside mail view with content
          document.querySelector('#inside-mail-view').innerHTML = 
          `<div id="mail"> <div> <b>From</b>: ${sender} </div> <div> <button id="btn1" class="btn btn-secondary">Reply</button> <button id="btn" class="btn btn-secondary"> ${arch}</button> </div></div> <br> <b>To</b>: ${recipients} <br><br> <b>Subject</b>: ${subject} <br><br><br> ${body} <br> ${time}`
          //Check if the archive button is clicked or not
          document.querySelector('#btn').addEventListener('click', () => archive(id, archived));
          //Check if the reply button is clicked or not
          document.querySelector('#btn1').addEventListener('click', () => reply_mail(sender, subject, body, time));
        });

        //Appending the email as a div into the main view
        if (mailbox === 'sent'){
          document.querySelector('#emails-view').append(div);
        } else {
          document.querySelector(`.OG${counter}`).append(div, btn);
        } 
        
        //Doing the styling based if it is read or not 
        if (read === false) {
          document.querySelector(`.OG${counter}`).style.backgroundColor = "white";
        } else {
          document.querySelector(`.OG${counter}`).style.backgroundColor = "gray";
        }
        
      });
  });
}

//Function for archiving and unarchiving then loading inbox
function archive(id, archived) {
  let flag
  if (archived === false) {
    flag = true
  } else {
    flag = false
  }
  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
        archived: flag
    })
  })
  load_mailbox('inbox');
  window.location.reload();
}

function reply_mail (sender, subject, body, time) {
    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#inside-mail-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';
  
    // Clear out composition fields
    document.querySelector('#compose-recipients').value = sender;
    document.querySelector('#compose-subject').value = `Re: ${subject}`;
    document.querySelector('#compose-body').value = `On ${time} ${sender} wrote: ${body}`;
}

function send_email() {

  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: document.querySelector('#compose-recipients').value,
        subject: document.querySelector('#compose-subject').value,
        body: document.querySelector('#compose-body').value
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      console.log(result);
  });
  localStorage.clear();
  //window.location.reload();
  load_mailbox('sent');
  //took me 1 hour to figure out this return false so my page does not refresh and go to main page
  //Apparently when we are submiting a form it is looking for an href to go to. So if there is none 
  //It will automatically refresh the page. So return false so it does not do that 
  return false;
}