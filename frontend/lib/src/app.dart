import 'package:flutter/material.dart';
import 'package:genosdocs_ui/src/constants/theme.dart';
import 'screens/home_screen.dart';

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Home',
      home: const HomeScreen(),
      theme: AppTheme.lightTheme,
      themeMode: ThemeMode.system,
    );
  }
}
