/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let stockBought = false,
    totalProfit = 0,
    stockValue = 0;

  for (let i = 0; i < prices.length; i++) {
    if (stockBought) {
      if (
        prices[i] > prices[i + 1] ||
        (i === prices.length - 1 && prices[i] > stockValue)
      ) {
        totalProfit += prices[i] - stockValue;
        stockBought = false;
        stockValue = 0;
      }
    } else {
      if (prices[i] < prices[i + 1]) {
        stockValue = prices[i];
        stockBought = true;
      }
    }
  }

  return totalProfit;
};

console.log(maxProfit([1, 2, 3, 4, 5]));
