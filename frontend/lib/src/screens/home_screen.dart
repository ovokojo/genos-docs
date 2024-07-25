import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'analytics_page.dart';
import 'dashboard_screen.dart';
import 'knowledge_base_screen.dart';
import 'settings_page.dart';
import '../widgets/custom_drawer.dart';
import '../providers/app_state.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  final List<Widget> _pages = const [
    DashboardScreen(),
    KnowledgeBaseScreen(),
    AnalyticsScreen(),
    SettingsScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    final appState = Provider.of<AppState>(context);
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: Icon(appState.isDrawerOpen ? Icons.menu_open : Icons.menu),
          onPressed: appState.toggleDrawer,
        ),
      ),
      body: Row(
        children: [
          if (appState.isDrawerOpen) const CustomDrawer(),
          Expanded(
            child: _pages[appState.selectedIndex],
          ),
        ],
      ),
    );
  }
}
