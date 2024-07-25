import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'src/providers/app_state.dart';
import 'src/app.dart';

void main() {
  runApp(
    ChangeNotifierProvider(
      create: (context) => AppState(),
      child: const MainApp(),
    ),
  );
}
