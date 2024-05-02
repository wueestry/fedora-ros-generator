# Meta Package
Name:           ros-jazzy-qt-dotgraph
Version:        2.7.4
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/qt_dotgraph
Summary:        Meta package for ros2-jazzy-qt_dotgraph and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-qt_dotgraph
Requires:       ros2-jazzy-qt_dotgraph-devel

Obsoletes: ros-jazzy-qt-dotgraph < 2.7.4-1

%description
qt_dotgraph provides helpers to work with dot graphs.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.7.4-1
- Update to latest release
