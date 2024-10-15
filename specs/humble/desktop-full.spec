# Meta Package
Name:           ros-humble-desktop-full
Version:        0.10.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-desktop_full and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-desktop_full
Requires:       ros2-humble-desktop_full-devel

Obsoletes: ros-humble-desktop-full < 0.10.0-1

%description
Provides a "batteries included" experience to novice users.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.10.0-1
- Update to latest release
