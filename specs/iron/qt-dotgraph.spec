# Meta Package
Name:           ros-iron-qt-dotgraph
Version:        2.4.3
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/qt_dotgraph
Summary:        Meta package for ros2-iron-qt_dotgraph and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-qt_dotgraph
Requires:       ros2-iron-qt_dotgraph-devel

Obsoletes: ros-iron-qt-dotgraph < 2.4.3-1

%description
qt_dotgraph provides helpers to work with dot graphs.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.4.3-1
- Update to latest release
