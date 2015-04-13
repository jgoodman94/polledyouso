$(function() {
    //$("#login").hide();
    var currentId;
    qs = generateQs();
    if (qs.length == 0) {
        alert("no questions! create a question");
    }
    qs.first({
        success: function(object) {
            updateQ(object);
        },
        error: function(error) {
            alert("Error: " + error.code + " " + error.message);
        }
    });
    // get id of page; need to store this question id somewhere on the page, this is just hardcoded
    
    
    $('.answer.display').click(function() {
        answerQ(this);
    })
    
    $('#navLeft').click(function() {
        moveQ("left", qs);
    })
    
    $('#navRight').click(function() {
        moveQ("right", qs);
    })
});

// qs returned as a Parse collection
function generateQs() {
    var qs = [];
    var Questions = Parse.Object.extend("Questions");
    var query = new Parse.Query(Questions);
    return query;
}

function answerQ(elmt) {
    // generate map
    ansarr = {};
    ansarr["answer_one"] = "one_answers";
    ansarr["answer_two"] = "two_answers";
    ansarr["answer_three"] = "three_answers";
    ansarr["answer_four"] = "four_answers";
    ansarr["answer_five"] = "five_answers";
    
    var colval = $(elmt).attr('id');
    console.log("selected "+colval);
    var Questions = Parse.Object.extend("Questions");
    var thisq = new Parse.Query(Questions);
    thisq.equalTo("objectId", currentId);
    //console.log("we made it");
    thisq.find({
        success: function(results) {
            // do something
            if (results.length == 1) {
                // should maybe add a mechanism that complains if result is already there
                results[0].add(ansarr[colval], Parse.User.current().id);
                results[0].save()
                console.log("problema risposta a");
            }
            else {
                alert("ci e male qualcosa con questo problema (something went wrong)");
            }
            
        },
        error: function(error) {
            alert("la vostra risponsa non stati registrata");
        }
    });
    moveQ("right");
}

// move either left or right in question display
function moveQ(direction) {
    qs.descending("objectId"); // would be better to sort by location, and date
    qs.find({
        success: function(results) {
            for (var i=0;i<results.length;i++) {
                if (results[i].id == currentId) {
                    if (direction == "left") {
                        var t = i - 1;
                        if (i == 0) {
                            t = results.length - 1;
                        }
                    }
                    else { // if direction == "right"
                        var t = i + 1;
                        if (i == results.length - 1) {
                            t = 0;
                        }
                    }
                }
            }
            updateQ(results[t]);
        },
        error: function(error) {
            alert("non potevamo trovare la domanda seguente");
        }
    });
}

// update page to refer to newq
function updateQ(newq) {
    $("#question").text(newq.get("question"));
    updateAnswerField("answer_one", newq);
    updateAnswerField("answer_two", newq);
    updateAnswerField("answer_three", newq);
    updateAnswerField("answer_four", newq);
    updateAnswerField("answer_five", newq);
    currentId = newq.id;
    console.log("current id is "+currentId);
}

function updateAnswerField(sel, newq) {
    var id = '#' + sel;
    if (newq.get(sel) != "") {
        $(id).text(newq.get(sel));
        $(id).show();
    }
    else {
        $(id).hide();
        // block question in, perhaps, with purple
        console.log(sel + " is hidden");
    }
}
