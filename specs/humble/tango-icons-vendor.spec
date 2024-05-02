# Meta Package
Name:           ros-humble-tango-icons-vendor
Version:        0.1.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://ros.org/wiki/qt_gui_icons
Summary:        Meta package for ros2-humble-tango_icons_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-tango_icons_vendor
Requires:       ros2-humble-tango_icons_vendor-devel

Obsoletes: ros-humble-tango-icons-vendor < 0.1.1-1

%description
tango_icons_vendor provides the public domain Tango icons for non-
linux systems (

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.1.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.1.1-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.1.1-1
- Initial humble build
