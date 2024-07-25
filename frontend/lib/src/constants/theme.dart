import 'package:flutter/material.dart';
import 'colors.dart';

class AppTheme {
  static ThemeData get lightTheme {
    return ThemeData(
      primaryColor: AppColors.lightPrimary,
      scaffoldBackgroundColor: AppColors.lightBackground,
      appBarTheme: const AppBarTheme(
        backgroundColor: AppColors.lightBackground,
        foregroundColor: AppColors.lightText,
      ),
      textTheme: const TextTheme(
        bodyLarge: TextStyle(color: AppColors.lightText),
        bodyMedium: TextStyle(color: AppColors.lightText),
      ),
      iconTheme: const IconThemeData(
        color: AppColors.lightPrimary,
      ),
      buttonTheme: ButtonThemeData(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
        buttonColor: AppColors.lightPrimary,
        textTheme: ButtonTextTheme.primary,
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          foregroundColor: AppColors.lightTextLight,
          backgroundColor: AppColors.lightPrimary,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
        ),
      ),
      inputDecorationTheme: InputDecorationTheme(
        hintStyle: TextStyle(color: AppColors.lightText.withOpacity(0.6)),
        fillColor: AppColors.lightBackground,
        filled: true,
        border: const OutlineInputBorder(
          borderSide: BorderSide(color: AppColors.lightPrimary),
        ),
        enabledBorder: OutlineInputBorder(
          borderSide: BorderSide(color: AppColors.lightPrimary.withOpacity(0.5)),
        ),
        focusedBorder: const OutlineInputBorder(
          borderSide: BorderSide(color: AppColors.lightPrimary, width: 2),
        ),
        prefixIconColor: AppColors.lightPrimary,
      ),
      progressIndicatorTheme: const ProgressIndicatorThemeData(
        color: AppColors.lightPrimary,
      ),
      // Add more theme properties as needed
    );
  }

  static ThemeData get darkTheme {
    return ThemeData(
      primaryColor: AppColors.darkPrimary,
      scaffoldBackgroundColor: AppColors.darkBackground,
      appBarTheme: const AppBarTheme(
        backgroundColor: AppColors.darkPrimary,
        foregroundColor: AppColors.darkText,
      ),
      textTheme: const TextTheme(
        bodyLarge: TextStyle(color: AppColors.darkText),
        bodyMedium: TextStyle(color: AppColors.darkText),
      ),
      iconTheme: const IconThemeData(
        color: AppColors.darkPrimary,
      ),
      inputDecorationTheme: InputDecorationTheme(
        hintStyle: TextStyle(color: AppColors.darkText.withOpacity(0.6)),
        fillColor: AppColors.darkBackground,
        filled: true,
        border: const OutlineInputBorder(
          borderSide: BorderSide(color: AppColors.darkPrimary),
        ),
        enabledBorder: OutlineInputBorder(
          borderSide: BorderSide(color: AppColors.darkPrimary.withOpacity(0.5)),
        ),
        focusedBorder: const OutlineInputBorder(
          borderSide: BorderSide(color: AppColors.darkPrimary, width: 2),
        ),
        prefixIconColor: AppColors.darkPrimary,
      ),
      // Add more theme properties as needed
    );
  }
}
