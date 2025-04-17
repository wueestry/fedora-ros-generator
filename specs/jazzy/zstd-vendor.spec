# Meta Package
Name:           ros-jazzy-zstd-vendor
Version:        0.26.6
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://facebook.github.io/zstd/
Summary:        Meta package for ros2-jazzy-zstd_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-zstd_vendor
Requires:       ros2-jazzy-zstd_vendor-devel

Obsoletes: ros-jazzy-zstd-vendor < 0.26.6-1

%description
Zstd compression vendor package, providing a dependency for Zstd.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.6-1
- Update to latest release
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.5-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.4-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.26.2-1
- Update to latest release
