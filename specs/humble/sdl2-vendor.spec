# Meta Package
Name:           ros-humble-sdl2-vendor
Version:        3.3.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-sdl2_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-sdl2_vendor
Requires:       ros2-humble-sdl2_vendor-devel

Obsoletes: ros-humble-sdl2-vendor < 3.3.0-1

%description
Vendor library for SDL2.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.3.0-1
- update to latest upstream
* Sat Oct 21 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.2.0-1
- update to latest upstream
