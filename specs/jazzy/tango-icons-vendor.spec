# Meta Package
Name:           ros-jazzy-tango-icons-vendor
Version:        0.3.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://ros.org/wiki/qt_gui_icons
Summary:        Meta package for ros2-jazzy-tango_icons_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-tango_icons_vendor
Requires:       ros2-jazzy-tango_icons_vendor-devel

Obsoletes: ros-jazzy-tango-icons-vendor < 0.3.0-1

%description
tango_icons_vendor provides the public domain Tango icons for non-
linux systems (

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.3.0-1
- Update to latest release
