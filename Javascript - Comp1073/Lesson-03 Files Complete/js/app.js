var output = document.querySelector('body p:nth-of-type(2)');
//console.log(output);
/* STEP 1: Creating an array
When declaring and initializing an array, you can include strings, numbers, booleans, and even other arrays */
var myArray = ['string', true, 100, [1, 3, 5]];
output.textContent = myArray;

/* STEP 2: Reading and changing array elements
You can refer to a particular element in an array with it's index number */
output.textContent = myArray[2];
// You can also change a particular element
myArray[1] = false;
output.textContent = myArray[1];
// An array within an array is called a multidimensional array - it can be accessed by specifying the index of the first array, then the item within it
output.textContent = myArray[3][2];
/* STEP 3: Determining array length
Being able to figure out how many elements are contained in an array is a critical feature of JavaScript programming */
output.textContent = myArray.length;
// In particular, looping through arrays
for (var i = 0; i < myArray.length; i++) {
    console.log(myArray[i]);
    output.textContent += ', ' + myArray[i];
}

/* STEP 4: Convert a string to an array
If there is a common character that can act as a delimiter in a string, we can use this character to create an array */
var origSix = 'Toronto Maple Leafs, Chicago Black Hawks, Detroit Red Wings, Boston Bruins, Montreal Canadiens';
var origSixArray = origSix.split(', ');
console.log(origSixArray);
// Output one of the array items
output.textContent = origSixArray[0];
// Output the last element of the array
output.textContent = origSixArray[origSixArray.length - 1];
/* STEP 5: Convert an array back to a string
Use join() and toString() - note that join() allows you to choose and insert a delimiter, while toString() does not */
var origSixString = origSixArray.join(' - ');
output.textContent = origSixString;
origSixString = origSixArray.toString();
output.textContent = origSixString;
/* STEP 6: Adding and removing items from an array
Without the ability to edit the contents of an array, this type of variable would have limited use - but adding and removing array items is pretty straightforward */

// Adding one or more items to an array with push()
//origSixArray.push('New York Rangers');
//output.textContent = origSixArray;
// If you would like to capture how many elements are in the array after you have edited it, then…
var origSixLength = origSixArray.push('New York Rangers', 'Philadelphia Flyers');
output.textContent = origSixLength + ' items, and they are...' + origSixArray;
// Removing an item from an array with pop()
// origSixArray.pop();
// output.textContent = origSixArray;
// pop() returns the item that was removed, rather than the length of the updated array, so…
var itemRemoved = origSixArray.pop();
output.textContent = 'We removed ' + itemRemoved + ' from the origSixArray, which is now... ' + origSixArray;
// To do the same thing, that is, to add and remove an item from the beginning of the array, use shift() and unshift()
origSixLength = origSixArray.unshift('Buffalo Sabres');
output.textContent = origSixLength + ' ... ' + origSixArray;
itemRemoved = origSixArray.shift();
output.textContent = 'We removed ' + itemRemoved + ' and the array now contains: ' + origSixArray;
/* That's it for the basics of working with arrays! With these tools at your disposal, a whole new world of possibilities with JavaScript are at your command */
