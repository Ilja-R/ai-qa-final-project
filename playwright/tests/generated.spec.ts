import { test, expect } from '@playwright/test';

test('Valid login navigates to Products page', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await expect(page).toHaveURL('https://www.saucedemo.com/');

  await page.fill('#user-name', 'standard_user');
  await expect(page.locator('#user-name')).toHaveValue('standard_user');

  await page.fill('#password', 'secret_sauce');
  await expect(page.locator('#password')).toHaveValue('secret_sauce');

  await page.click('#login-button');
  await expect(page).toHaveURL('https://www.saucedemo.com/inventory.html');
});

test('Invalid password shows error message', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await expect(page).toHaveURL('https://www.saucedemo.com/');

  await page.fill('#user-name', 'standard_user');
  await expect(page.locator('#user-name')).toHaveValue('standard_user');

  await page.fill('#password', 'wrong_password');
  await expect(page.locator('#password')).toHaveValue('wrong_password');

  await page.click('#login-button');
  await expect(page.locator('.error-message-container')).toBeVisible();
});

test('Invalid username shows error message', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await expect(page).toHaveURL('https://www.saucedemo.com/');

  await page.fill('#user-name', 'invalid_user');
  await expect(page.locator('#user-name')).toHaveValue('invalid_user');

  await page.fill('#password', 'secret_sauce');
  await expect(page.locator('#password')).toHaveValue('secret_sauce');

  await page.click('#login-button');
  await expect(page.locator('.error-message-container')).toBeVisible();
});

test('Empty fields show error message', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await expect(page).toHaveURL('https://www.saucedemo.com/');

  await expect(page.locator('#user-name')).toHaveValue('');
  await expect(page.locator('#password')).toHaveValue('');

  await page.click('#login-button');
  await expect(page.locator('.error-message-container')).toBeVisible();
});

test('Locked user shows locked user error', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await expect(page).toHaveURL('https://www.saucedemo.com/');

  await page.fill('#user-name', 'locked_out_user');
  await expect(page.locator('#user-name')).toHaveValue('locked_out_user');

  await page.fill('#password', 'secret_sauce');
  await expect(page.locator('#password')).toHaveValue('secret_sauce');

  await page.click('#login-button');
  await expect(page.locator('.error-message-container')).toBeVisible();
});