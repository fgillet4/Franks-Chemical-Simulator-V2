pub fn add(left: usize, right: usize) -> usize {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}

use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

// src/lib.rs
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn calculate_friction_loss(length: f64, diameter: f64, flow_rate: f64, roughness: f64, viscosity: f64) -> f64 {
    // Darcy-Weisbach equation variables
    let velocity = flow_rate / (std::f64::consts::PI * (diameter / 2.0).powi(2));
    let reynolds_number = (velocity * diameter) / viscosity;
    let friction_factor = 0.079 / reynolds_number.powf(0.25); // Using Blasius equation (valid for 3000 < Re < 100,000)

    // Darcy-Weisbach equation to calculate head loss
    (friction_factor * length * velocity.powi(2)) / (2.0 * diameter * 9.81)
}
