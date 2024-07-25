import 'package:flutter/foundation.dart';

class AppState with ChangeNotifier {
  int _selectedIndex = 1;
  bool _isDrawerOpen = true;

  int get selectedIndex => _selectedIndex;
  bool get isDrawerOpen => _isDrawerOpen;

  void setSelectedIndex(int index) {
    _selectedIndex = index;
    notifyListeners();
  }

  void toggleDrawer() {
    _isDrawerOpen = !_isDrawerOpen;
    notifyListeners();
  }
}
