import { test, expect } from '@playwright/test';

test('Valid login with correct credentials', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await page.fill('#user-name', 'standard_user');
  await expect(page.locator('#user-name')).toHaveValue('standard_user');
  await page.fill('#password', 'secret_sauce');
  await expect(page.locator('#password')).toHaveValue('secret_sauce');
  await page.click('#login-button');
  await expect(page.locator('.inventory_list')).toBeVisible();
});

test('Invalid password login', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await page.fill('#user-name', 'standard_user');
  await expect(page.locator('#user-name')).toHaveValue('standard_user');
  await page.fill('#password', 'wrong_password');
  await expect(page.locator('#password')).toHaveValue('wrong_password');
  await page.click('#login-button');
  await expect(page.locator('.error-message-container')).toBeVisible();
});

test('Invalid username login', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await page.fill('#user-name', 'invalid_user');
  await expect(page.locator('#user-name')).toHaveValue('invalid_user');
  await page.fill('#password', 'secret_sauce');
  await expect(page.locator('#password')).toHaveValue('secret_sauce');
  await page.click('#login-button');
  await expect(page.locator('.error-message-container')).toBeVisible();
});

test('Empty username and password fields', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await expect(page.locator('#user-name')).toBeEmpty();
  await expect(page.locator('#password')).toBeEmpty();
  await page.click('#login-button');
  await expect(page.locator('.error-message-container')).toBeVisible();
});

test('Empty username field with valid password', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await expect(page.locator('#user-name')).toBeEmpty();
  await page.fill('#password', 'secret_sauce');
  await expect(page.locator('#password')).toHaveValue('secret_sauce');
  await page.click('#login-button');
  await expect(page.locator('.error-message-container')).toBeVisible();
});

test('Empty password field with valid username', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await page.fill('#user-name', 'standard_user');
  await expect(page.locator('#user-name')).toHaveValue('standard_user');
  await expect(page.locator('#password')).toBeEmpty();
  await page.click('#login-button');
  await expect(page.locator('.error-message-container')).toBeVisible();
});

test('Locked user login attempt', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await page.fill('#user-name', 'locked_out_user');
  await expect(page.locator('#user-name')).toHaveValue('locked_out_user');
  await page.fill('#password', 'secret_sauce');
  await expect(page.locator('#password')).toHaveValue('secret_sauce');
  await page.click('#login-button');
  await expect(page.locator('.error-message-container')).toBeVisible();
});