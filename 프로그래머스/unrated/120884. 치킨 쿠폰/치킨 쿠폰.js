function solution(chicken) {
    var coupon = chicken;
    let s_chick = Math.floor(coupon / 10)
    let total = s_chick
    let d = coupon % 10
    while (coupon >= 10) {
         coupon = s_chick;
         coupon += d
         s_chick = Math.floor(coupon / 10)
         total += s_chick
         d = coupon % 10
    }
    return total;
}