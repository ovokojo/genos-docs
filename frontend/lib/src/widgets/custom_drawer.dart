import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/app_state.dart';

class CustomDrawer extends StatelessWidget {
  const CustomDrawer({super.key});

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    return Consumer<AppState>(
      builder: (context, AppState appState, child) {
        return SizedBox(
          width: 250,
          child: Drawer(
            child: ListView(
              padding: EdgeInsets.zero,
              children: <Widget>[
                SizedBox(
                  height: 50,
                  child: DrawerHeader(
                    padding: const EdgeInsets.all(10),
                    decoration: BoxDecoration(
                      color: theme.primaryColor,
                    ),
                    child: const Text('Genos Docs'),
                  ),
                ),
                _buildDrawerItem(context, 'Dashboard', 0),
                _buildDrawerItem(context, 'Knowledge Base', 1),
                _buildDrawerItem(context, 'Analytics', 2),
                _buildDrawerItem(context, 'Settings', 3),
              ],
            ),
          ),
        );
      },
    );
  }

  Widget _buildDrawerItem(BuildContext context, String title, int index) {
    final theme = Theme.of(context);
    final appState = Provider.of<AppState>(context);
    bool isSelected = appState.selectedIndex == index;
    return ListTile(
      leading: Icon(
        _getDrawerIcon(index),
        color: theme.primaryColor,
      ),
      title: Text(
        title,
        style: TextStyle(
          color: isSelected ? theme.primaryColor : Colors.black,
          fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
        ),
      ),
      selected: isSelected,
      onTap: () => appState.setSelectedIndex(index),
      tileColor: isSelected ? theme.primaryColor.withOpacity(0.1) : Colors.transparent,
    );
  }

  IconData _getDrawerIcon(int index) {
    if (index == 0) {
      return Icons.dashboard;
    } else if (index == 1) {
      return Icons.library_books;
    } else if (index == 2) {
      return Icons.analytics;
    } else if (index == 3) {
      return Icons.settings;
    } else {
      return Icons.question_mark;
    }
  }
}
