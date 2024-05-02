# Meta Package
Name:           ros-iron-tango-icons-vendor
Version:        0.2.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://ros.org/wiki/qt_gui_icons
Summary:        Meta package for ros2-iron-tango_icons_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-tango_icons_vendor
Requires:       ros2-iron-tango_icons_vendor-devel

Obsoletes: ros-iron-tango-icons-vendor < 0.2.2-1

%description
tango_icons_vendor provides the public domain Tango icons for non-
linux systems (

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.2.2-1
- Update to latest release
