function lowerBound(arr, target) {
  let start = 0;
  let end = arr.length;

  let mid;
  while (start < end) {
    mid = Math.floor((start + end) / 2);
    if (arr[mid] >= target) {
      end = mid;
    } else {
      start = mid + 1;
    }
  }
  return end;
}

function upperBound(arr, target) {
  let start = 0;
  let end = arr.length;
  let mid;
  console.log(end);
  while (start < end) {
    mid = Math.floor((start + end) / 2);
    if (arr[mid] > target) {
      end = mid;
    } else {
      start = mid + 1;
    }
  }
  return end;
}

const arr = [1, 2, 2, 2, 3, 3, 4, 4, 4];
console.log(upperBound(arr, 2));
console.log(lowerBound(arr, 2));
